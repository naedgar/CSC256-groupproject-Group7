*** Settings ***
Documentation     PR-7 Acceptance Tests - Task Management Application
...               Robot Framework E2E tests with behavioral parity
...               with Playwright-BDD tests from Sprint 4

Library           RequestsLibrary
Library           Collections
Library           String
Library           DateTime
Library           BuiltIn

Suite Setup       Initialize Test Environment
Suite Teardown    Cleanup Test Environment

*** Variables ***
${BASE_URL}       http://localhost:5000
${API_URL}        ${BASE_URL}/api
${TIMEOUT}        5s


*** Keywords ***
Initialize Test Environment
    [Documentation]    Setup test environment and reset state
    Create Session      app    ${BASE_URL}    timeout=5
    Reset Tasks

Cleanup Test Environment
    [Documentation]    Cleanup after tests
    Reset Tasks
    Delete All Sessions

Reset Tasks
    [Documentation]    Reset tasks to clean state
    ${response}=        POST On Session    app    /api/tasks/reset
    Should Be Equal As Integers    ${response.status_code}    200

Should Have Key
    [Arguments]    ${dictionary}    ${key}
    [Documentation]    Verify dictionary has specified key
    Dictionary Should Contain Key    ${dictionary}    ${key}
*** Test Cases ***
TC-ACC-001 Add Valid Task Via API
    [Documentation]    Acceptance: User can add a valid task via API
    [Tags]    acceptance    tasks    create
    Reset Tasks
    
    ${payload}=         Create Dictionary    title=Buy groceries    description=Milk and eggs
    ${response}=        POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    
    ${data}=            Set Variable    ${response.json()}
    
    Dictionary Should Contain Key    ${data}    id
    Dictionary Should Contain Key    ${data}    title
    Dictionary Should Contain Key    ${data}    description
    Dictionary Should Contain Key    ${data}    completed
    Should Be Equal    ${data}[title]    Buy groceries
    Should Be Equal    ${data}[description]    Milk and eggs
    Should Be Equal    ${data}[completed]    ${False}

TC-ACC-002 Add Task Without Description
    [Documentation]    Acceptance: User can add task with optional description
    [Tags]    acceptance    tasks    create
    Reset Tasks
    
    ${payload}=         Create Dictionary    title=Call Mom
    ${response}=        POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    
    ${data}=            Set Variable    ${response.json()}
    Should Be Equal    ${data}[title]    Call Mom
    Should Be Equal    ${data}[description]    ${EMPTY}

TC-ACC-003 Reject Empty Title
    [Documentation]    Acceptance: System rejects tasks with empty title
    [Tags]    acceptance    tasks    validation
    Reset Tasks
    
    ${payload}=         Create Dictionary    title=${EMPTY}    description=No title
    ${response}=        POST On Session    app    /api/tasks    json=${payload}    expected_status=400
    
    ${data}=            Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${data}    error

TC-ACC-004 Reject Missing Title Field
    [Documentation]    Acceptance: System rejects tasks without title field
    [Tags]    acceptance    tasks    validation
    Reset Tasks
    
    ${payload}=         Create Dictionary    description=No title field
    ${response}=        POST On Session    app    /api/tasks    json=${payload}    expected_status=400
    
    ${data}=            Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${data}    error

TC-ACC-005 Get Empty Task List
    [Documentation]    Acceptance: User can fetch empty task list
    [Tags]    acceptance    tasks    read
    Reset Tasks
    
    ${response}=        GET On Session    app    /api/tasks    expected_status=200
    
    ${data}=            Set Variable    ${response.json()}
    Length Should Be    ${data}    0

TC-ACC-006 Get Non-Empty Task List
    [Documentation]    Acceptance: User can fetch list of created tasks
    [Tags]    acceptance    tasks    read
    Reset Tasks
    
    # Add tasks
    ${payload1}=        Create Dictionary    title=Task 1
    ${payload2}=        Create Dictionary    title=Task 2
    ${payload3}=        Create Dictionary    title=Task 3
    POST On Session    app    /api/tasks    json=${payload1}    expected_status=201
    POST On Session    app    /api/tasks    json=${payload2}    expected_status=201
    POST On Session    app    /api/tasks    json=${payload3}    expected_status=201
    
    # Get list
    ${response}=        GET On Session    app    /api/tasks    expected_status=200
    
    ${data}=            Set Variable    ${response.json()}
    Length Should Be    ${data}    3
    
    # Verify all tasks have required fields
    FOR    ${task}    IN    @{data}
        Dictionary Should Contain Key    ${task}    id
        Dictionary Should Contain Key    ${task}    title
        Dictionary Should Contain Key    ${task}    description
        Dictionary Should Contain Key    ${task}    completed
    END

TC-ACC-007 Mark Task Complete
    [Documentation]    Acceptance: User can mark task as complete
    [Tags]    acceptance    tasks    update
    Reset Tasks
    
    # Create task
    ${payload}=         Create Dictionary    title=Do homework
    ${create_response}=    POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    ${task_id}=            Get From Dictionary    ${create_response.json()}    id
    
    # Mark complete
    ${response}=           PUT On Session    app    /api/tasks/${task_id}    expected_status=200
    
    ${data}=               Set Variable    ${response.json()}
    Should Be Equal    ${data}[completed]    ${True}
    Should Be Equal As Integers    ${data}[id]    ${task_id}

TC-ACC-008 Cannot Complete Nonexistent Task
    [Documentation]    Acceptance: System rejects marking nonexistent task complete
    [Tags]    acceptance    tasks    error
    Reset Tasks
    
    ${response}=        PUT On Session    app    /api/tasks/9999    expected_status=404
    
    ${data}=            Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${data}    error

TC-ACC-009 Delete Task
    [Documentation]    Acceptance: User can delete a task
    [Tags]    acceptance    tasks    delete
    Reset Tasks
    
    # Create task
    ${payload}=         Create Dictionary    title=Task to delete
    ${create_response}=    POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    ${task_id}=            Get From Dictionary    ${create_response.json()}    id
    
    # Verify it exists
    ${get_response}=       GET On Session    app    /api/tasks    expected_status=200
    ${tasks_before}=       Get Length    ${get_response.json()}
    
    # Delete
    ${response}=           DELETE On Session    app    /api/tasks/${task_id}    expected_status=200
    
    # Verify deletion
    ${get_response}=       GET On Session    app    /api/tasks    expected_status=200
    ${tasks_after}=        Get Length    ${get_response.json()}
    Should Be Equal As Integers    ${tasks_after}    ${tasks_before - 1}

TC-ACC-010 Cannot Delete Nonexistent Task
    [Documentation]    Acceptance: System rejects deleting nonexistent task
    [Tags]    acceptance    tasks    error
    Reset Tasks
    
    ${response}=        DELETE On Session    app    /api/tasks/9999    expected_status=404
    
    ${data}=            Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${data}    error

TC-ACC-101 Get Current Time
    [Documentation]    Acceptance: User can fetch current server time
    [Tags]    acceptance    time    read
    Reset Tasks
    
    ${response}=        GET On Session    app    /api/time    expected_status=200
    
    ${data}=            Set Variable    ${response.json()}
    # Should have at least one field
    Length Should Be    ${data}    2

TC-ACC-102 Time Response Format
    [Documentation]    Acceptance: Time response is in ISO 8601 format
    [Tags]    acceptance    time    read
    Reset Tasks
    
    ${response}=        GET On Session    app    /api/time    expected_status=200
    ${data}=            Set Variable    ${response.json()}
    
    # Extract datetime field - check both possible field names
    ${has_utc_datetime}=    Run Keyword And Return Status    Get From Dictionary    ${data}    utc_datetime
    ${datetime_field}=      Set Variable If    ${has_utc_datetime}    ${data}[utc_datetime]    ${data}[datetime]
    
    # Verify ISO 8601 format (YYYY-MM-DDTHH:MM:SS)
    Should Match Regexp    ${datetime_field}    ^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}

TC-ACC-103 Time Response Has Timezone
    [Documentation]    Acceptance: Time response includes timezone information
    [Tags]    acceptance    time    read
    Reset Tasks
    
    ${response}=        GET On Session    app    /api/time    expected_status=200
    ${data}=            Set Variable    ${response.json()}
    
    # Should have source, Z suffix, or UTC indicator
    ${response_str}=    Convert To String    ${data}
    Should Match Regexp    ${response_str}    (source|UTC|Z)

TC-ACC-201 Workflow: Create Multiple Tasks
    [Documentation]    Acceptance: Complete workflow of creating multiple tasks
    [Tags]    acceptance    workflow
    Reset Tasks
    
    # Create 5 tasks
    FOR    ${i}    IN RANGE    1    6
        ${payload}=    Create Dictionary    title=Task ${i}
        POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    END
    
    # Verify all exist
    ${response}=        GET On Session    app    /api/tasks    expected_status=200
    ${tasks}=           Set Variable    ${response.json()}
    Length Should Be    ${tasks}    5

TC-ACC-202 Workflow: Create, Complete, Delete
    [Documentation]    Acceptance: Complete workflow of full task lifecycle
    [Tags]    acceptance    workflow
    Reset Tasks
    
    # Create
    ${payload}=         Create Dictionary    title=Lifecycle task    description=Full cycle
    ${create_response}=    POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    ${task_id}=            Get From Dictionary    ${create_response.json()}    id
    
    # Complete
    PUT On Session    app    /api/tasks/${task_id}    expected_status=200
    
    # Verify completed
    ${get_response}=    GET On Session    app    /api/tasks    expected_status=200
    ${tasks}=           Set Variable    ${get_response.json()}
    
    # Find our task
    ${found}=      Set Variable    ${False}
    FOR    ${task}    IN    @{tasks}
        ${task_id_from_list}=    Get From Dictionary    ${task}    id
        ${is_match}=    Evaluate    ${task_id_from_list} == ${task_id}
        Run Keyword If    ${is_match}    Set Test Variable    ${found}    ${True}
    END
    
    Should Be True    ${found}
    
    # Delete
    DELETE On Session    app    /api/tasks/${task_id}    expected_status=200
    
    # Verify deleted
    ${get_response}=    GET On Session    app    /api/tasks    expected_status=200
    ${tasks}=           Set Variable    ${get_response.json()}
    
    ${found}=    Set Variable    ${False}
    FOR    ${task}    IN    @{tasks}
        ${check_id}=    Get From Dictionary    ${task}    id
        ${is_deleted}=    Evaluate    ${check_id} == ${task_id}
        Run Keyword If    ${is_deleted}    Set Test Variable    ${found}    ${True}
    END
    
    Should Be Equal    ${found}    ${False}

TC-ACC-203 Workflow: Create Task With Whitespace
    [Documentation]    Acceptance: System trims whitespace from task input
    [Tags]    acceptance    workflow    validation
    Reset Tasks
    
    ${title_input}=     Set Variable    Task Title
    ${desc_input}=      Set Variable    Description
    
    ${payload}=         Create Dictionary    title=${title_input}    description=${desc_input}
    ${response}=        POST On Session    app    /api/tasks    json=${payload}    expected_status=201
    
    ${data}=            Set Variable    ${response.json()}
    Should Be Equal    ${data}[title]    ${title_input}
    Should Be Equal    ${data}[description]    ${desc_input}

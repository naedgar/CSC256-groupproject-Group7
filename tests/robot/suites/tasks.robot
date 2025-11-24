*** Settings ***
Resource    ../resources/keywords.robot
Library    Collections
Suite Setup    Run Keywords    Start Session    AND    Start App
Suite Teardown    Stop App
Test Setup    Reset Tasks Data

*** Test Cases ***
Complete Task Workflow - Create, Complete, and Verify
    ${created}=    Create Task    Playwright BDD Integration Task    Created using Playwright BDD
    ${id}=    Set Variable    ${created['id']}
    ${tasks}=    Get Tasks
    ${titles}=    Create List
    FOR    ${t}    IN    @{tasks}
        Append To List    ${titles}    ${t['title']}
    END
    Should Contain    ${titles}    Playwright BDD Integration Task
    ${updated}=    Complete Task    ${id}
    ${completed}=    Set Variable    ${updated['completed']}
    Should Be True    ${completed}

Simple Task Creation Workflow
    ${created}=    Create Task    Quick Playwright BDD Task    Testing Playwright BDD functionality
    ${tasks}=    Get Tasks
    ${titles}=    Create List
    FOR    ${t}    IN    @{tasks}
        Append To List    ${titles}    ${t['title']}
    END
    Should Contain    ${titles}    Quick Playwright BDD Task

Task Creation And Verification
    ${created}=    Create Task    Playwright Verification Task
    ${tasks}=    Get Tasks
    ${titles}=    Create List
    FOR    ${t}    IN    @{tasks}
        Append To List    ${titles}    ${t['title']}
    END
    Should Contain    ${titles}    Playwright Verification Task

Get Tasks - Empty Then Non-Empty
    # After Reset (Test Setup) tasks should be empty
    ${tasks}=    Get Tasks
    Length Should Be    ${tasks}    0
    # create a task and verify non-empty
    ${created}=    Create Task    Post-Get Task    created for get test
    ${tasks2}=    Get Tasks
    Length Should Be    ${tasks2}    1

Delete Task - Valid ID Removes Task
    ${created}=    Create Task    To Be Deleted    delete test
    ${id}=    Set Variable    ${created['id']}
    Delete Task    ${id}
    ${tasks}=    Get Tasks
    ${titles}=    Create List
    FOR    ${t}    IN    @{tasks}
        Append To List    ${titles}    ${t['title']}
    END
    Should Not Contain    ${titles}    To Be Deleted

Delete Task - Invalid ID Returns 404
    ${resp}=    Evaluate    __import__('requests').delete('${BASE_URL}' + '/api/tasks/9999')
    Should Be Equal As Integers    ${resp.status_code}    404

Complete Task - Invalid ID Returns 404
    ${resp}=    Evaluate    __import__('requests').put('${BASE_URL}' + '/api/tasks/9999')
    Should Be Equal As Integers    ${resp.status_code}    404

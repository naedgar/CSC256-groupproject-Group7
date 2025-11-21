*** Settings ***
Library    RequestsLibrary
Library    Process

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000
${SESSION}     api

*** Keywords ***
Start Session
    Create Session    ${SESSION}    ${BASE_URL}

Start App
    ${handle}=    Start Process    python3    -m    app.main    stdout=NONE    stderr=NONE    shell=False
    Set Suite Variable    ${APP_PROC}    ${handle}
    Wait For Server

Stop App
    Run Keyword If    ${APP_PROC}    Terminate Process    ${APP_PROC}
    Sleep    0.5s

Wait For Server
    Wait Until Keyword Succeeds    1 min    2 sec    Get Health Should Be Ok

Get Health Should Be Ok
    ${http_proxy}=    Evaluate    __import__('os').environ.get('HTTP_PROXY','')
    ${https_proxy}=    Evaluate    __import__('os').environ.get('HTTPS_PROXY','')
    ${no_proxy}=    Evaluate    __import__('os').environ.get('NO_PROXY','')
    Log    HTTP_PROXY=${http_proxy} HTTPS_PROXY=${https_proxy} NO_PROXY=${no_proxy}
    ${status}    ${result}=    Run Keyword And Ignore Error    GET On Session    ${SESSION}    /api/health
    Log    Health call status=${status}
    Log    Health call result=${result}
    Run Keyword If    '${status}' != 'PASS'    Fail    Health request failed: ${result}
    ${resp}=    Set Variable    ${result}
    Log    ${resp.text}
    Should Be Equal As Integers    ${resp.status_code}    200

Reset Tasks Data
    ${resp}=    POST On Session    ${SESSION}    /api/tasks/reset
    Should Be Equal As Integers    ${resp.status_code}    200

Create Task
    [Arguments]    ${title}    ${description}=
    ${payload}=    Create Dictionary    title=${title}    description=${description}
    ${resp}=    POST On Session    ${SESSION}    /api/tasks    json=${payload}
    Should Be Equal As Integers    ${resp.status_code}    201
    ${body_text}=    Set Variable    ${resp.text}
    ${body}=    Evaluate    __import__('json').loads(r'''${body_text}''')
    RETURN    ${body}

Create Unique Task
    [Arguments]    ${prefix}    ${description}=
    ${now}=    Evaluate    int(__import__('time').time()*1000)
    ${title}=    Set Variable    ${prefix} - ${now}
    ${body}=    Create Task    ${title}    ${description}
    RETURN    ${body}

Find Task By Title
    [Arguments]    ${title}
    ${tasks}=    Get Tasks
    ${matches}=    Evaluate    [t for t in tasks if t.get('title')==title]
    Run Keyword If    ${matches}    Return From Keyword    ${matches}[0]
    Return From Keyword    ${NONE}

Seed Tasks
    [Arguments]    ${count}=3    ${prefix}=seed
    FOR    ${i}    IN RANGE    ${count}
        Create Unique Task    ${prefix}
    END

Get Tasks
    ${resp}=    GET On Session    ${SESSION}    /api/tasks
    Should Be Equal As Integers    ${resp.status_code}    200
    ${body_text}=    Set Variable    ${resp.text}
    ${body}=    Evaluate    __import__('json').loads(r'''${body_text}''')
    RETURN    ${body}

Get Time
    ${resp}=    GET On Session    ${SESSION}    /api/time
    # allow either 200 or 500-like handling depending on app
    ${code}=    Set Variable    ${resp.status_code}
    Run Keyword If    '${code}' != '200'    Fail    Time endpoint returned status ${code}
    ${body_text}=    Set Variable    ${resp.text}
    ${body}=    Evaluate    __import__('json').loads(r'''${body_text}''')
    RETURN    ${body}

Assert Time Fields Present
    [Arguments]    ${body}
    Run Keyword If    'error' in str(${body})    Fail    TimeService returned error: ${body}
    # Accept either 'datetime' (legacy) or 'utc_datetime' (fallback)
    Run Keyword Unless    'datetime' in str(${body}) or 'utc_datetime' in str(${body})    Fail    TimeService returned unexpected payload: ${body}

Complete Task
    [Arguments]    ${task_id}
    ${resp}=    PUT On Session    ${SESSION}    /api/tasks/${task_id}
    Should Be Equal As Integers    ${resp.status_code}    200
    ${body_text}=    Set Variable    ${resp.text}
    ${body}=    Evaluate    __import__('json').loads(r'''${body_text}''')
    RETURN    ${body}

Delete Task
    [Arguments]    ${task_id}
    ${resp}=    DELETE On Session    ${SESSION}    /api/tasks/${task_id}
    ${code}=    Set Variable    ${resp.status_code}
    Run Keyword If    '${code}' == '200'    No Operation    ELSE    Fail    Task delete failed with status ${code}

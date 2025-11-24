*** Settings ***
Resource    ../resources/keywords.robot
Library     Collections
Suite Setup    Run Keywords    Start Session    AND    Start App
Suite Teardown    Stop App
Test Setup    Reset Tasks Data

*** Test Cases ***
Create Task - Missing Title Returns 400
    ${payload}=    Create Dictionary
    ${resp}=    Evaluate    __import__('requests').post('${BASE_URL}' + '/api/tasks', json=${payload})
    Should Be Equal As Integers    ${resp.status_code}    400
    ${body}=    Evaluate    __import__('json').loads(r'''${resp.text}''')
    Should Contain    ${body}    error
    Should Contain    ${body}    field
    Should Be Equal    ${body['field']}    title

Create Task - Empty Title Returns 400
    ${payload}=    Create Dictionary    title=   description=some
    ${resp}=    Evaluate    __import__('requests').post('${BASE_URL}' + '/api/tasks', json=${payload})
    Should Be Equal As Integers    ${resp.status_code}    400
    ${body}=    Evaluate    __import__('json').loads(r'''${resp.text}''')
    Should Contain    ${body}    error
    Should Be Equal    ${body['field']}    title

Create Task - Title Too Long Returns 400
    ${long_title}=    Evaluate    'x'*300
    ${payload}=    Create Dictionary    title=${long_title}
    ${resp}=    Evaluate    __import__('requests').post('${BASE_URL}' + '/api/tasks', json=${payload})
    Should Be Equal As Integers    ${resp.status_code}    400
    ${body}=    Evaluate    __import__('json').loads(r'''${resp.text}''')
    Should Contain    ${body}    error
    Should Be Equal    ${body['field']}    title

Create Task - Description Too Long Returns 400
    ${long_desc}=    Evaluate    'd'*600
    ${payload}=    Create Dictionary    title=Valid Title    description=${long_desc}
    ${resp}=    Evaluate    __import__('requests').post('${BASE_URL}' + '/api/tasks', json=${payload})
    Should Be Equal As Integers    ${resp.status_code}    400
    ${body}=    Evaluate    __import__('json').loads(r'''${resp.text}''')
    Should Contain    ${body}    error
    Should Be Equal    ${body['field']}    description

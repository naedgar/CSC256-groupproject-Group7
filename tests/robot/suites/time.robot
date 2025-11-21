*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Run Keywords    Start Session    AND    Start App
Suite Teardown    Stop App

*** Test Cases ***
Time Service Returns datetime and timezone
    ${body}=    Get Time
    Assert Time Fields Present    ${body}

Time Service Graceful Error Handling
    ${body}=    Get Time
    # If the service returns an error payload, ensure it's the graceful message
    ${has_error}=    Evaluate    'error' in ${body}
    Run Keyword If    ${has_error}    Should Contain    ${body}['error']    Unable
    Run Keyword Unless    ${has_error}    Assert Time Fields Present    ${body}

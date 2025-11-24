*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Health Endpoint Direct Test
    [Documentation]    Create a session and call /api/health directly to debug RequestsLibrary behavior.
    ${base}=    Set Variable    http://127.0.0.1:5000
    ${alias}=   Set Variable    debug_session
    Create Session    ${alias}    ${base}
    ${proxies}=    Evaluate    __import__('requests').utils.get_environ_proxies('${base}')
    Log    proxies=${proxies}
    ${status}    ${result}=    Run Keyword And Ignore Error    GET On Session    ${alias}    /api/health
    Log    health_status=${status}
    Log    health_result=${result}
    Run Keyword If    '${status}' == 'PASS'    Log    status_code=${result.status_code}
    Run Keyword If    '${status}' == 'PASS'    Log    body=${result.text}
    Run Keyword If    '${status}' != 'PASS'    Fail    GET on session failed: ${result}

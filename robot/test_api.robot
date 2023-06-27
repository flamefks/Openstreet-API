*** Settings ***
Library     api.py

*** Test Cases ***
Limit val
    ${limit}=  get_limit  ${3}
    Should Be Equal    ${limit}  ${3}

Limit max
    ${max}=  get_limit  ${51}
    Should Be Equal    ${max}  ${50}

Limit default
    ${default}=  get_limit
    Should Be Equal        ${default}  ${10}

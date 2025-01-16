*** Keywords ***
Capture Evidence On Failure
    Run Keyword If Test Failed    Capture Page Screenshot    ${TEST NAME}_failure.png

*** Keywords ***
Log Test Details
    Log    Executing test on ${BROWSER} browser    console=yes
    Log    Using test data: ${TEST DATA}    level=DEBUG

# Organize reports with timestamps
robot --outputdir reports/$(date +%Y%m%d_%H%M%S) tests/
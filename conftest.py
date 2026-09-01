import pytest
from pathlib import Path

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make the test result available to fixtures.
    This allows us to check if a test failed in our screenshot fixture.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def _failure_screenshot_and_trace(page, request):
    """
    Automatically capture a screenshot on failure and save it to screenshots/.
    """
    yield
    
    # Check if the test failed during the 'call' phase
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # 1. Capture Screenshot
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        
        # Create a clean filename from the test name
        test_name = request.node.name.replace("/", "_").replace(":", "_").replace("[", "_").replace("]", "_")
        screenshot_path = screenshot_dir / f"{test_name}_failure.png"
        
        # Save screenshot
        page.screenshot(path=str(screenshot_path))

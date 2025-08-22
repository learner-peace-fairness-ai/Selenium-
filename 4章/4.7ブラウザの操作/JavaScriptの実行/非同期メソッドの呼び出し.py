from selenium import webdriver

WAIT_SECONDS = 3

with webdriver.Edge() as driver:
    driver.set_script_timeout(WAIT_SECONDS)
    val = 1

    result = driver.execute_async_script(
        """
        const WAIT_MILLI_SEC = 1000;
        const callback = arguments[arguments.length - 1];
        const arg = arguments[0];
        setTimeout(callback(arg * 2), WAIT_MILLI_SEC);
    """,
        val,
    )
    print(result)

from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
import os


load_dotenv('.env.credentials')

def context_manager(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        load_dotenv('env.local_emulator')

        options.set_capability('remote_url', os.getenv('LOCAL_REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))

    if context == 'bstack':
        load_dotenv('.env.bstack')

        options.set_capability('remote_url', os.getenv('BS_REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability(
            'bstack:options', {
                "projectName": "Baze project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack test",
                "userName": os.getenv('BS_USER_NAME'),
                "accessKey": os.getenv('BS_ACCESS_KEY'),
            },
        )
    return options
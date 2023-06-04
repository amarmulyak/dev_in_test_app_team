from environs import Env


env = Env()
env.read_env(verbose=True)

TIMEOUT = env.int('TIMEOUT')
POLLING = env.float('POLLING')

EMAIL = env.str('EMAIL')
PASSWORD = env.str('PASSWORD')

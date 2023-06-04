from environs import Env


env = Env()
env.read_env(verbose=True)

EMAIL = env.str('EMAIL')
PASSWORD = env.str('PASSWORD')

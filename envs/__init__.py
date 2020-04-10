from gym.envs.registration import register

register(
    id="WfedBipedal-v0",
    entry_point="envs.wfed_bipedal_env:WfedBIpedalEnv"
)

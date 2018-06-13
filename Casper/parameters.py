"""List of parameters for the simulation.
"""

NUM_VALIDATORS = 50  # number of validators at each checkpoint
VALIDATOR_IDS = list(range(0, NUM_VALIDATORS))  # set of validators
INITIAL_VALIDATORS = list(range(0, NUM_VALIDATORS))  # set of validators for root
BLOCK_PROPOSAL_TIME = 100  # adds a block every 100 ticks
EPOCH_SIZE = 5  # checkpoint every 5 blocks
AVG_LATENCY = 100  # will be modified in metrics

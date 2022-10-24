# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## ------- import packages -------
from dwave.system import LeapHybridCQMSampler
from dimod import ConstrainedQuadraticModel, Binary

# TODO:  Add code here to define your BQM
def get_cqm(S):
    """Returns a dictionary representing a QUBO.

    Args:
        S (list of integers): the value for each box
    """

    cqm = ConstrainedQuadraticModel()

    # Define binary variables

    # Set CQM objective

    # Add CQM constraint
    
    return cqm

def run_on_hss(cqm, sampler):
    """Runs the CQM on the sampler provided.

    Args:
        cqm (ConstrainedQuadraticModel): a CQM for the problem
        sampler (dimod.Sampler): a hybrid solver
    """

    sample_set = sampler.sample(cqm, label='Training - Choosing Boxes')

    return sample_set

## ------- Main program -------
if __name__ == "__main__":

    S = [17, 21, 19]

    cqm = get_cqm(S)

    #TODO:  Write code to define your sampler

    #TODO:  Write code to run your problem

    #TODO:  Write code to look at the solutions returned

# For example, the third line of the file is "74 59", indicating that
# the second job has weight 74 and length 59. You should NOT assume
# that edge weights or lengths are distinct.

# Your task in this problem is to run the greedy algorithm that
# schedules jobs in decreasing order of the difference (weight -
# length). Recall from lecture that this algorithm is not always
# optimal. IMPORTANT: if two jobs have equal difference (weight -
# length), you should schedule the job with higher weight
# first. Beware: if you break ties in a different way, you are likely
# to get the wrong answer. 
# You should report the sum of weighted
# completion times of the resulting schedule --- a positive integer
# --- in the box below.

# ADVICE: If you get the wrong answer, try out some small test cases
# to debug your algorithm (and post your test cases to the discussion
# forum)!

import os

class Job:
    def __repr__(self):
        return "{weight: "+str(self.weight)+", length: "+str(self.length)+", diff: "+str(self.diff)+", ratio: "+str(self.ratio)+"}"

    def __init__(self, line):
        job_data = map(int, line.split())
        self.weight = job_data[0]
        self.length = job_data[1]
        self.diff = self.weight - self.length
        self.ratio = float(self.weight)/self.length

    def __eq__(self, other):
        return self.weight == other.weight and self.length == other.length

    def cmp_diff(job_a, job_b):
        """compare two jobs. if two jobs have equal difference (weight -
        length), you should schedule the job with higher weight
        first.

        """
        if job_a.diff == job_b.diff:
            return -1 if job_a.weight > job_b.weight else 1
        return -1 if job_a.diff > job_b.diff else 1

    def cmp_ratio(job_a, job_b):
        """compare two jobs by their ratio
        """
        return -1 if job_a.ratio > job_b.ratio else 1
        
def test():
    a  = [Job("4 2"), Job("5 3"), Job("4 1"), Job("3 1")]
    ar = [Job("4 1"), Job("5 3"), Job("4 2"), Job("3 1")]
    a.sort(Job.cmp_diff)
    if a != ar:
        raise Exception('list did not sort properly')
    return True

test()

def parse_jobs(sort_fn):
    "return set of jobs with "
    f = open('jobs.txt', 'r');
    #f = open('jobs_test.txt', 'r');   # remove! 
    num_jobs = int(f.readline())

    jobs = map(Job, f.readlines())
    if len(jobs) != num_jobs:
        raise Exception('wrong number of jobs excpected %d got %i' % (num_jobs, len(jobs)))
    jobs.sort(sort_fn)
    return jobs    

def weighted_completion_time(jobs):
    w = 0
    t = 0
    for j in jobs:
        t = t + j.length
        w = w + t*j.weight
    return w

def schedule_jobs():
    """Your task in this problem is to run the greedy algorithm that
schedules jobs in decreasing order of the difference (weight -
length). Recall from lecture that this algorithm is not always
optimal. IMPORTANT: if two jobs have equal difference (weight -
length), you should schedule the job with higher weight first. Beware:
if you break ties in a different way, you are likely to get the wrong
answer. You should report the sum of weighted completion times of the
resulting schedule --- a positive integer --- in the box below."""
    jobs_diff = parse_jobs(Job.cmp_diff)
    jobs_ratio = parse_jobs(Job.cmp_ratio)
    return [weighted_completion_time(x) for x in [jobs_diff, jobs_ratio]]
    
# 69119377652
# 67311454237

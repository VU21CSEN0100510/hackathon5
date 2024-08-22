import hashlib
import random

class ElectronicVotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.voters = {}
        self.total_votes = 0

    def register_voter(self, voter_id):
        token = hashlib.sha256(str(random.random()).encode()).hexdigest()
        self.voters[voter_id] = {"token": token, "has_voted": False}
        return token

    def cast_vote(self, voter_id, candidate_index):
        if voter_id in self.voters:
            if not self.voters[voter_id]["has_voted"]:
                if 0 <= candidate_index < len(self.candidates):
                    self.votes[self.candidates[candidate_index]] += 1
                    self.voters[voter_id]["has_voted"] = True
                    print("\nVote casted successfully. Thank you for participating.\n")
                else:
                    print("\nInvalid choice. Please try again.\n")
            else:
                print("\nError: You have already voted.\n")
        else:
            print("\nError: Invalid voter ID.\n")

    def display_results(self):
        print("\nFinal Voting Results:\n")
        for candidate, vote_count in self.votes.items():
            print(f"Candidate: {candidate} - Votes: {vote_count}")
        print(f"\nTotal Votes: {self.total_votes}")
candidates = ["Aa", "Bb", "Cc"]
evs = ElectronicVotingSystem(candidates)
n = int(input("Register the number of voters: "))
for i in range(n):
    voter_id = input(f"Voter {i + 1} ID: ")
    evs.register_voter(voter_id)
print("\n--- Voting Begins ---")
for i in range(n):
    voter_id = input("\nEnter your Voter ID: ")
    print("Choose your candidate:")
    for index, candidate in enumerate(candidates, start=1):
        print(f"{index}. {candidate}")
    candidate_index = int(input("Your choice (enter the number): ")) - 1
    evs.cast_vote(voter_id, candidate_index)
evs.display_results()

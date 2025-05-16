"""
721. Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is
some common email to both accounts. Note that even if two accounts have the same name, they may belong to
different people as people could have the same name. A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account
is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned
in any order.
"""

"""
Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph = defaultdict(set)  # email -> set of neighboring emails
        email_to_name = {}

        # Build email graph first
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                # need both direction so that it allows us to go from first_email -> email_1 -> email_2
                # otherwise if it starts from email_1, it can only go from email_1 -> email_2 and miss first_email
                email_graph[first_email].add(email)
                email_graph[email].add(first_email)
                email_to_name[email] = name
                email_to_name[first_email] = name

        # Traverse with BFS
        seen = set()
        merged = []

        for email in email_graph:
            if email in seen:
                continue
            queue = deque([email])
            component = []

            while queue:
                node = queue.popleft()
                if node in seen:
                    continue
                seen.add(node)
                component.append(node)
                queue.extend(email_graph[node])

            merged.append([email_to_name[email]] + sorted(component))

        return merged


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        # Union emails within the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                dsu.union(first_email, email)
                email_to_name[email] = name

        # Collect emails by root parent
        groups = defaultdict(list)
        for email in email_to_name:
            root = dsu.find(email)
            groups[root].append(email)

        # Build merged results
        merged = []
        for root, emails in groups.items():
            name = email_to_name[root]
            merged.append([name] + sorted(emails))

        return merged

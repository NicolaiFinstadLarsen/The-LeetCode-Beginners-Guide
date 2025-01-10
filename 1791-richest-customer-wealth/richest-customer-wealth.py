class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        counter = 0
        for element in accounts:
            counter += 1
        #print(counter)

        account_sum = []
        for i in range(0,counter):
            account_sum.append(sum(accounts[i]))
            #print(max(account_sum))
        return max(account_sum)


# Not my solution, I need to learn map. 
# It maps the sum to each element in accounts. That element beeing a sublist.
# class Solution:
    #def maximumWealth(self, accounts: List[List[int]]) -> int:
        #return max(map(sum, accounts))
        
# Represent forces on dominos (dominos are represented by a char in a string):
class Solution(object):
    def pushDominos(self, dominoes):
        forces = [0] * len(dominoes)
        max_force = len(dominoes)

        # Move from right to left:
        force = 0
        for i, d in enumerate(dominoes):
            if d == 'R':
                force == max_force
            if d == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] = force

        # Move from left to right:
        for i in range(len(dominoes) - 1, -1, -1):
            d = dominoes[i]
            if d == 'L':
                force == max_force
            if d == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force     # go back in the dominoes

        # Construct the result:
        result = ''
        for f in forces:
            if f == 0:
                result += '.'
            elif f > 0:
                result += 'R'
            else:
                result + 'L'
        return result



print(Solution().pushDominos('..R...L..R'))
# ..RR..LL..RR

from typing import List, Optional

# In the pattern, one letter corresponds to one letter
# The pattern square matrix window will be parsed through the board matrix
# Return the lowest-row (or lowest-column if rows are equal) top-left corner location of the matching matrix, otherwise return [-1, -1]
def solve(board: List[List[int]], pattern: List[List[str]]) -> List[int]:
    res: List[List[int]] = []
    plen = len(pattern)

    hm: dict[str, List[List[int]]] = {}

    for r in range(plen):
        for c in range(plen):
            val = pattern[r][c]
            if val not in hm.keys():
                hm[val] = [[r, c]]
            else:
                hm[val].append([r, c])

    for r in range(len(board)):
        for c in range(len(board[0])):
            if r + plen - 1 < len(board) and c + plen - 1 < len(board[0]):
                isValid: bool = True
                topLeft: List[int] = [r, c]

                for key, value in hm.items():
                    if not isValid:
                        break

                    if key.isnumeric():
                        for coords in value:
                            x, y = coords[0], coords[1]
                            if board[r+x][c+y] != int(key):
                                isValid = False
                                break
                    elif len(value) > 1:
                        curr: Optional[int] = None

                        for coords in value:
                            x, y = coords[0], coords[1]
                            if not curr:
                                curr = board[x+r][y+c]
                            elif curr != board[x+r][y+c]:
                                isValid = False
                                break

                if isValid:
                    res.append(topLeft)


    print(sorted(res))
    return res

b: List[List[int]] = [[2,4,2,4,2], [4,1,4,2,2],[1,4,2,5,3]]
p: List[List[str]] = [["4", "c"], ["c", "b"]]

print(solve(b, p))

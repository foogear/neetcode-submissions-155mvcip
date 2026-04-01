class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image, sr, sc, color):
            if image[sr][sc] == color:
                return None
            currentColor = image[sr][sc]
            image[sr][sc] = color
            
            canGoUp   = sr - 1 >= 0
            canGoDown = sr + 1 <= len(image) - 1
            canGoLeft = sc - 1 >= 0
            canGoRight = (len(image) > 0) and (sc + 1 <= len(image[0]) - 1)


            if canGoUp and    image[sr-1][sc] == currentColor:
                ##print(         f"up{sr-1}{sc}")
                dfs(image,          sr-1, sc, color)
            if canGoDown and  image[sr+1][sc] == currentColor:
                ##print(       f"down{sr+1}{sc}")
                dfs(image,          sr+1, sc, color)
            if canGoLeft and  image[sr][sc-1] == currentColor:
                ##print(       f"left{sr}{sc-1}")
                dfs(image,          sr, sc-1, color)
            if canGoRight and image[sr][sc+1] == currentColor:
                ##print(      f"right{sr}{sc+1}")
                dfs(image,          sr, sc+1, color)

            ##print("fin")
            return None
        
        dfs(image, sr, sc, color)
        return image
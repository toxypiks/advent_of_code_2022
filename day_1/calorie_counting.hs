import System.IO  
import Control.Monad

split :: Eq a => a -> [a] -> [[a]]
split x y = func x y [[]]
    where
        func x [] z = reverse $ map (reverse) z
        func x (y:ys) (z:zs) = if y==x then 
            func x ys ([]:(z:zs)) 
        else 
            func x ys ((y:z):zs)

elfes :: [String] -> [[String]] -> [[String]]
elfes [] [] = []
elfes (x:[]) [] = [[x]]
elfes (x:xs) [] = elfes xs [[x]]
elfes [] (y:ys) |y == [] = ys
                |otherwise = (y:ys)
elfes (x:xs) (y:ys) | x /= "" = elfes xs ((x:y):ys) 
                    | otherwise = elfes xs ([]:(y:ys))

main = do  
        let list = []
        handle <- openFile "input_small.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = split '\n' contents
            list = elfes singlewords []
        print list
        hClose handle   

f :: [String] -> [Int]
f = map read

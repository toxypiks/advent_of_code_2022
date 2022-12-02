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

elves :: [String] -> [[String]] -> [[String]]
elves [] [] = []
elves (x:[]) [] = [[x]]
elves (x:xs) [] = elves xs [[x]]
elves [] (y:ys) |y == [] = ys
                |otherwise = (y:ys)
elves (x:xs) (y:ys) | x /= "" = elves xs ((x:y):ys)
                    | otherwise = elves xs ([]:(y:ys))

main = do  
        let list = []
        handle <- openFile "input_small.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = split '\n' contents
            list = elves singlewords []
        print $ foldr max 0 (map (sum . (map read)) list)
        hClose handle   

f :: [String] -> [Int]
f = map read

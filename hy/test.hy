#!/home/xuhui/venv3/bin/hy 
(require [hy.contrib.walk [let]])
(let [x 1]
 (print x)
 (let [x 33]
   (print x)
   (setv x 44)
   (print x)
 (printx))


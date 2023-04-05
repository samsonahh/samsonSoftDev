#lang racket

(define fact (lambda (n)
  (if ( < n 2 )
    1
  (* n (fact (- n 1))))))

(fact 4)

(define fib (lambda (n)
  (if ( < n 2)
      1
  (+ (fib(- n 1)) (fib(- n 2))))))

(fib 4)
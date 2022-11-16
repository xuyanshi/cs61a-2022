(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1)
    )
  )

(define (make-adder num)
  (lambda (inc) (+ inc num))
  )

(define (composed f g)
  (lambda (x) (f (g x)))
  )

(define lst
   (cons (cons 1 nil)
        (cons 2
              (cons (cons 3 (cons 4 nil))
                    (cons 5 nil))))
  )

(define (duplicate lst) 'YOUR-CODE-HERE)

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

(define (composed f g) 'YOUR-CODE-HERE)

(define lst 'YOUR-CODE-HERE)

(define (duplicate lst) 'YOUR-CODE-HERE)

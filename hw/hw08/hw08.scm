(define (my-filter pred lst)
  (cond
          ((null? lst) lst)
          ((pred (car lst))(cons (car lst) (my-filter pred (cdr lst))))
          (else (my-filter pred (cdr lst)))
          )
  )

(define (interleave lst1 lst2) 'YOUR-CODE-HERE)

(define (accumulate joiner start n term)
  'YOUR-CODE-HERE)

(define (no-repeats lst) 'YOUR-CODE-HERE)

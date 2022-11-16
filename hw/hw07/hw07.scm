(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst)
  (cond
    ((null? asc-lst) #t)
    ((null? (cdr asc-lst)) #t)
    ( (or (< (car asc-lst) (cadr asc-lst)) (= (car asc-lst) (cadr asc-lst)) )
      (ascending? (cdr asc-lst))
      )
    (else #f)
    ))

(define (square n) (* n n))

(define (pow base exp) 'YOUR-CODE-HERE)

;Implementation of lsts and common lst functions in scheme

(define (filter func lst)
    (cond ((null? lst) lst)
        ((func (car lst)) (cons (car lst) (filter func (cdr lst))))
        (else (filter func (cdr lst)))
    )
)

(define (map func lst)
    (if (null? lst)
        lst
        (cons (func (car lst)) (map func (cdr lst)))
    )
)

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (len lst)
    (if (null? lst)
        0
        (+ 1 (len (cdr lst)))
    )
)

(define (maxlst lst)
    (cond ((null? (cdr lst)) (car lst))
        (else (if (> (car lst) (maxlst (cdr lst)))
                            (car lst)
                            (maxlst (cdr lst))
                            ))
    )
)

(define (minlst lst)
    (cond ((null? (cdr lst)) (car lst))
        (else (if (< (car lst) (minlst (cdr lst)))
                            (car lst)
                            (minlst (cdr lst))
                            ))
    )
)

(define (remove lst val)
    (cond ((null? lst) lst)
        ((= val (car lst)) (cdr lst))
        (else (cons (car lst) (remove (cdr lst) val)))
    )
)

(define (append lst1 lst2)
    (if (null? lst1)
        lst2
        (cons (car lst1) (append (cdr lst1) lst2))
    )
)

(define (index lst num)
    (if (= num 0)
        (car lst)
        (index (cdr lst) (- num 1))
    )
)

(define (getindex lst num)
    (cond ((null? lst) 1)
        ((= (car lst) num) 0)
        (else (+ 1 (getindex (cdr lst) num)))
    )
)

; count is untested
(define (count list elem)
    (len (filter (list (lambda (x) (= x elem)))))
)


(define (sort lst)
    (if (= 1 (len lst))
        lst
        (append (sort (remove lst (maxlst lst))) (lst (maxlst lst)))
    )
)

(define (sort2 lst)
    (if (= 1 (len lst))
        lst
        (cons (minlst lst) (remove lst (minlst lst)))
    )
)

(define (quicksort lst)
    (if (or (null? lst) (null? (cdr lst)))
        lst
        (append (append (quicksort (filter (lambda (x) (< x (car lst))) (cdr lst)))
                (lst (car lst)))
                (quicksort (filter (lambda (x) (>= x (car lst))) (cdr lst)))
        )
    )
)




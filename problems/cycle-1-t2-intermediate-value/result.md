# Result

Headline: A classical completeness proof establishes the intermediate value theorem for opposite-sign endpoints.

The direct statement is proved in `proofs/ivt.fml`. Endpoint-zero cases are immediate. In the strict-sign case, define S = {x in [a,b] : f(x) <= 0}; the least upper bound c exists by real completeness. Continuity at c rules out f(c)<0 and f(c)>0, so f(c)=0.

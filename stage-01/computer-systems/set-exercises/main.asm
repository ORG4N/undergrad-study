.386  ; Specify instruction set
.model flat, stdcall  ; Flat memory model, std. calling convention
.stack 4096 ; Reserve stack space
ExitProcess PROTO, dwExitCode: DWORD  ; Exit process prototype

.data 
	arrayA DWORD 10 DUP (?)	; create an array of size 10
	two DWORD 2
	seven DWORD 7

.code

main PROC ; main procedure

	mov esi, 0				; esi will store the index (which starts at 0)
	lea ebx, arrayA			; ebx will store the address of the first element of the array

	loop1:

	mov edx, 0				; this will discard the remainder of the divisions
	mov eax, esi			; load index into accumulator

	mul two					; multiply eax by 2
	add eax, seven			; add 7 to eax
	div two					; divide eax by 2

	mov [ebx + TYPE arrayA * esi], eax	; stores computed value back into the array

	inc esi					; increment the index
	cmp esi, 10				; this comparison is the ending condition
	jl loop1				; if the comparison = less than, branch to the loop1 label
	
	INVOKE ExitProcess, 0
  
main ENDP
END main
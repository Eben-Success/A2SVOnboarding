import sys, threading

def main():
    
    def fib(n):
        #fibonacci number
        
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        return fib(n - 1) + fib(n - 2)
    
    
sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
print(main.fib(6))


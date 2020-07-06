def function3():
    print("I'm Three!")
    function2()

def function1():
    print("I'm one!")

def function2():
    print("I'm Two!")



def function4():
    print("I'm Four")
    def function5():
        print("I'm five")
        def function6():
            print("I'm Six")
            def function7():
                print("I'm Seven")
        function6()
    function5()


function4()



def test_FirstTestName(request):
    testname = request.node.name
    print("\nTest Name is "+testname)
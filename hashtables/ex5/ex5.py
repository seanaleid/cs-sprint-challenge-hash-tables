# Your code here


def finder(files, queries):
    # initialize result list
    result = []
    # initialize dict
    d = dict()

    for idx, item in enumerate(files):
        output = item.split('/')
        # print(output)

        if output[-1] in d:
            d[output[-1]].append(files[idx])
        else:
            d[output[-1]] = [files[idx]]
    
    for query in queries:
        if query in d:
            for file in d[query]:
                result.append(file)
    
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

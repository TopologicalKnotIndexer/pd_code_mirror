import json
import pd_code_sanity

def mirror_pd_code(pd_code:list[list]) -> list[list]:

    # 检查是不是合法的 pd_code
    if not pd_code_sanity.sanity(pd_code):
        raise TypeError()
    
    pd_code = json.loads(json.dumps(pd_code))
    new_pd_code = [
        [crossing[0]] + crossing[3:0:-1]
        for crossing in pd_code
    ]

    if not pd_code_sanity.sanity(new_pd_code):
        raise AssertionError()
    
    return new_pd_code

if __name__ == "__main__":
    print(mirror_pd_code([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))

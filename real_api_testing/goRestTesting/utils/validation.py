def validate_json(expected_code,status_code,schema,json,Return_one):
        B=[False,False]
        id=None
        try:
            id=r.json()["id"]
        except:
            pass
        #validating test result
        try:
            s=self.schema_list[schema]
            print(s)
            validate(r.json(),s)
            B[1]=True
        except:
            pass
        if r.status_code == expected_code:
            B[0]=True
        print(return_only_bool)
        print(r.json())
        print()
        print(r.status_code)
        if return_only_bool:
            print()
            print()
            print(id,tuple(B))
            return True if B[0] and B[1] else False
        return id,tuple(B)

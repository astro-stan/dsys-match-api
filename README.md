# A simple python API for the dsys/match HTTP API.
A simple python API that can talk to the HTTP API of dsys/match

## Example usage:
```
import dsysmatch as dm

match = dm.DsysMatch("http://192.168.1.1")

result_dict = match.Add("./test.png", "test/path")
result_dict = match.Delete("test/path")
result_dict = match.Search("./test.png", True)
result_dict = match.Compare("./test.png", "./test.png")
result_dict = match.Count()
result_dict = match.List(2, 20)
result_dict = match.Ping()
```
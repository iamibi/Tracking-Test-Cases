# Tracking-Test-Cases
Tracking test cases is a work in progress tool that is being built
so that one can easily manage unit test cases. The idea is to generate a JSON
and then parse it to convert it to Excel. The JSON structure is

```
{
    "filename": {
        "pathToFile": String,
        "availableScenarios": [String],
        "tagStatus": String,
        "active": Boolean
    }
}
```

# TODO
1. Read data from files. 
2. Create a high level structure of JSON.
3. Check the activity status based on the changes in the test case.
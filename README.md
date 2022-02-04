
# labDAO Bio Runners

Example serverless "runners" that do biopython and other silly things for the LabDAO Bio Board. These are meant as examples to develop out the labDAO Workflow Runners ecosystem.

These examples run on Vercel Serverless /api/ endpoints, in a mix of python and node functions.




## Reverse Complement

Get the reverse complement of a genetic sequence. 

Ex: `CATGTAGACTAG` becomes `CTAGTCTACATG`. Implements Biopython's `reverse_complement()` function. 
- Type: API Provider (can be triggered with an POST request)
- URL: `/api/reverse-complement` (JSON Body data endpoint)
- URL: `/api/reverse-complement/form` (Form data endpoint)
- Usage: send a `POST` request with Form data, with "sequence" text field

Inputs: 
- `[name=sequence] form data field`
```javascript
// JSON body data
{
	sequence: "CAT"
}
```

Outputs:
```JSON
{
	"output": "ATG"
}
```

JSON Form body example:
```CURL
curl -X POST http://localhost:4500/api/reverse-complement -H "Content-Type: application/json" -d '{"sequence":"cat"}'

curl -X GET http://localhost:4500/api/reverse-complement?sequence=cat
```
Form data example:
```CURL
curl -X POST http://localhost:4500/api/reverse-complement/form -H "Content-Type: multipart/form-data" -F "sequence=CAT"
```

Future:
- Create a `GET` endpoint with `?sequence=CAT`
- Add IPFS support back, as an example
- Add a JSON body data endpoint as an example




### Async Endpoint

The Async endpoint can't be triggered directly by a job. Instead, it's triggered to "look at the next job" from the API endpoint, perform it, and post it back to the endpoint. It doesn't take take or respond with any data.


### Python Server / IPFS version

(Deprecated) this is an old experiment in both IPFS pinning and using Python Server. Kept around as an example.


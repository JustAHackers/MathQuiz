import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
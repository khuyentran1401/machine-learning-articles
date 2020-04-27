<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>$GH_REPOSITORY_DESCRIPTION</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta name="description" content="$GH_REPOSITORY_DESCRIPTION - $GH_REPOSITORY">
    <link rel="stylesheet" href="https://oleksis.github.io/machine-learning-articles/assets/css/style.css?v=b63269a076e29bc4df837b40ad0ba42e8326734f">
    <link rel='stylesheet' type='text/css' media='screen' href='build/main.css'>
    <script src='build/main.js'></script>
</head>
<body>
    <div class="container-lg px-3 my-5 markdown-body">
        <h1 id="machine-learning-articles">$GH_REPOSITORY</h1>
        <p>$GH_REPOSITORY_DESCRIPTION</p>
        <h2 id=list-mla></h2>
        <table role="table">
            <thead>
                <tr><th>Title</th><th>Labels</th><th>Author</th></tr>  
            </thead>
            <tbody>
                $ROWS_ISSUES
            </tbody>
        </table>
    </div>
</body>
</html>
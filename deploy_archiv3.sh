#!/bin/bash

do_deploy() {
    # Distributes an archive to a web server
    # Args:
    #   $1 (str): The path of the archive to distribute
    # Returns:
    #   If the file doesn't exist at archive_path or an error occurs - False
    #   Otherwise - True

    archive_path=$1
    file=$(basename "$archive_path")
    name="${file%.*}"

    if [[ ! -f $archive_path ]]; then
        return 1
    fi

    if ! $(scp "$archive_path" "/tmp/$file"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "rm -rf /data/web_static/releases/$name/"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "mkdir -p /data/web_static/releases/$name/"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "tar -xzf /tmp/$file -C /data/web_static/releases/$name/"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "rm /tmp/$file"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "mv /data/web_static/releases/$name/web_static/* /data/web_static/releases/$name/"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "rm -rf /data/web_static/releases/$name/web_static"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "rm -rf /data/web_static/current"); then
        return 1
    fi

    if ! $(ssh user@3.235.178.105 "ln -s /data/web_static/releases/$name/ /data/web_static/current"); then
        return 1
    fi

    return 0
}

# Call the function with the archive path as an argument
if do_deploy "/path/to/archive.tar.gz"; then
    echo "Archive distributed successfully"
else
    echo "Failed to distribute the archive"
fi


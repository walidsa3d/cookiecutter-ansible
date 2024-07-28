def remove_jinja_extensions():
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".j2"):
                new_name = filename[:-3]
                os.rename(os.path.join(root, filename), os.path.join(root, new_name))

if __name__ == "__main__":
    remove_jinja_extensions()
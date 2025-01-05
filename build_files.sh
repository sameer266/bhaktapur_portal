echo "BUILD START"

# Check Python version
python3.9 --version

# Upgrade pip and ensure it’s installed
python3.9 -m pip install --upgrade pip
python3.9 -m ensurepip 

# Install dependencies from requirements.txt
python3.9 -m pip install --no-cache-dir -r requirements.txt


echo "MAKE MIGRATIONS..."
# Make and apply migrations
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
python3.9 manage.py collectstatic --noinput

# List the contents of the staticfiles directory to verify
echo "Contents of staticfiles directory:"
ls -l staticfiles

echo "BUILD END"

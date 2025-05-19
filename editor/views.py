from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import tempfile
import os
import json

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        input_data = data.get('input', '')
        language = data.get('language', 'python')

        try:
            if language == 'python':
                ext = '.py'
                cmd = ['python', 'tempfile']
            elif language == 'javascript':
                ext = '.js'
                cmd = ['node', 'tempfile']
            else:
                return JsonResponse({'error': 'Language not supported.'})

            with tempfile.NamedTemporaryFile(mode='w', suffix=ext, delete=False) as temp:
                temp.write(code)
                temp_filename = temp.name

            cmd[1] = temp_filename
           # ...existing code...
            process = subprocess.Popen(
               cmd,
               stdin=subprocess.PIPE,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE,
               text=True
           )
            stdout, stderr = process.communicate(input=input_data)
# ...existing code...
            os.remove(temp_filename)

            return JsonResponse({
                'output': stdout,
                'error': stderr
            })

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import subprocess
# import json
# import tempfile
# import os
# from .models import CodeExecution

# @csrf_exempt
# def run_code(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         code = data.get('code')
#         input_data = data.get('input', '')

#         try:
#             # Use a temporary file for the code
#             with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp:
#                 temp.write(code)
#                 temp_filename = temp.name

#             # Execute the code using subprocess
#             process = subprocess.Popen(
#                 ['python', temp_filename],  # Use 'python' for Windows
#                 stdin=subprocess.PIPE,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE,
#                 text=True
#             )
#             stdout, stderr = process.communicate(input=input_data)

#             # Save execution to database
#             CodeExecution.objects.create(
#                 code=code,
#                 input_data=input_data,
#                 output_data=stdout
#             )

#             # Clean up the temp file
#             os.remove(temp_filename)

#             return JsonResponse({
#                 'output': stdout,
#                 'error': stderr
#             })

#         except Exception as e:
#             return JsonResponse({'error': str(e)})

#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
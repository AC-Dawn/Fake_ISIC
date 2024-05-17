document.addEventListener('DOMContentLoaded', function() {
	const submitButton = document.getElementById('submitButton');
	const nameInput = document.getElementById('nameInput');
	const dateInput = document.getElementById('dateInput');
	const fileInput = document.getElementById('fileInput');
	let uploadedFile = null;

    // 设置日期输入框

	 dateInput.addEventListener('click', function(event) {
	  	dateInput.showPicker();
	  });

	  const today = new Date().toISOString().split('T')[0];
	  dateInput.setAttribute('max', today);


  // 提交检查
  submitButton.addEventListener('click', async function() {
    if (!validateName(nameInput.value)) {
        alert('请输入英文名');
        return;
    }

    if (!dateInput.value) {
        alert('请选择生日');
        return;
    }

    // 获取用户上传的文件
    const file = fileInput.files[0];

    // 验证文件格式和大小
    const isValidFile = await validateFile(file);
    if (!isValidFile) {
        alert('上传文件格式(jpg,jpeg,png)或尺寸(210x253px)不符合要求');
        return;
    }

    // 如果文件验证通过，保存上传的文件
    uploadedFile = file;

    // 这里可以添加提交表单的逻辑，包括上传文件的逻辑
    submitForm(nameInput,dateInput,uploadedFile);

    });

});


function submitForm(nameInput,dateInput,uploadedFile) {

    const formData = new FormData();
    formData.append('name', nameInput.value);
    formData.append('birth', dateInput.value);
    formData.append('file', uploadedFile);

    fetch('/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
        } else {
          const filename = data.filename;
          document.getElementById('frontImage').src = `/outputs/${filename}`;
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
}



function validateName(name) {
	return /^[a-zA-Z\s]+$/.test(name);
}

function validateFile(file) {
    return new Promise(resolve => {
        if (!file) {
            resolve(false);
            return;
        }

        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];
        const targetWidth = 210;
        const targetHeight = 253;

        // 创建一个临时的Image对象用于获取图片尺寸
        const img = new Image();
        img.src = URL.createObjectURL(file);

        console.log(img)

        img.onload = function() {
            // 检查图片类型是否合法
            if (!allowedTypes.includes(file.type)) {
                resolve(false);
                return;
            }

            // 检查图片尺寸是否合法
            if (img.width === targetWidth && img.height === targetHeight) {
                resolve(true);
            } else {
                resolve(false);
            }
        };

        img.onerror = function() {
            resolve(false);
        };
    });
}

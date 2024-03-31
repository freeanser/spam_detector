// scripts.js

const currentUser = 'You';
const socket = io.connect('http://your-server-address');

function scrollToBottom() {
  $('#chatBox').scrollTop($('#chatList').height());
}

function predict() {
  let message = $('#messageInput').val();

  $.ajax({
    type: 'POST',
    url: '/predict',
    data: { 'message': message },
    beforeSend: function () {
      $('#loading').show();
    },
    success: function (response) {
      $('#loading').hide();
      displayResult(response.prediction);

      const predictionText = response.prediction == 1 ? 'This is a Spam.' : 'It is a Ham.';
      $('#chatList').append(`<li class="user" id="${currentUser}">${currentUser}: <br> ${message}</li>`);
      $('#chatList').append(`<li class="bot">Bot: <br>${predictionText}</li>`);

      // 使用延遲來確保在新增消息後再進行滾動
      setTimeout(function () {
        scrollToBottom();
      }, 100);

      socket.emit('user_prediction', { prediction: response.prediction, message: message });
    },
    error: function (error) {
      $('#loading').hide();
      console.log('Error:', error);
    }
  });
}

function displayResult(prediction) {
  let resultContainer = $('#resultContainer');
  resultContainer.empty();

  let resultText = (prediction == 1) ? 'This is a Spam.' : 'It is a Ham.';

  resultContainer.append('<h2 style="color: ' + (prediction == 1 ? 'red' : 'blue') + ';">' + resultText + '</h2>');
}


// const currentUser = 'You';
// const socket = io.connect('http://your-server-address');

// function predict() {
//   let message = $('#messageInput').val();

//   $.ajax({
//     type: 'POST',
//     url: '/predict',
//     data: { 'message': message },
//     beforeSend: function () {
//       $('#loading').show();
//     },
//     success: function (response) {
//       $('#loading').hide();
//       displayResult(response.prediction);

//       const predictionText = response.prediction == 1 ? 'This is a Spam.' : 'It is a Ham.';
//       $('#chatList').append(`<li class="user" id="${currentUser}">${currentUser}: <br> ${message}</li>`);
//       $('#chatList').append(`<li class="bot">Bot: <br>${predictionText}</li>`);
//       // 使用 socket.emit 發送預測結果到伺服器
//       socket.emit('user_prediction', { prediction: response.prediction, message: message });
//     },
//     error: function (error) {
//       $('#loading').hide();
//       console.log('Error:', error);
//     }
//   });
// }

// function displayResult(prediction) {
//   let resultContainer = $('#resultContainer');
//   resultContainer.empty();

//   let resultText = (prediction == 1) ? 'This is a Spam.' : 'It is a Ham.';

//   resultContainer.append('<h2 style="color: ' + (prediction == 1 ? 'red' : 'blue') + ';">' + resultText + '</h2>');
// }
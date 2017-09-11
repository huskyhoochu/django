# CSS 정복하기 (1)

## CSS와 박스 모델

### 박스 모델이란?

HTML의 모든 요소들은 상자로 이루어져 있고, 이것을 '박스 모델(box-model)'이라고 부른다. 박스는 다시 마진과 패딩, 테두리 등의 여러 겹의 박스들로 나뉜다.

![box model](https://pressupinc.com/wp-content/uploads/2014/01/box-model.png)

### 블록 레벨 요소와 인라인 레벨 요소

#### 블록 레벨 요소 (block-level)

블록 레벨 요소는 태그를 사용해 요소를 삽입했을 때 혼자 한 줄을 차지하는 요소다. 대표적으로 `<div>`태그와 `<p>`태그가 있다.

#### 인라인 레벨 요소 (inline-level)

인라인 레벨 요소는 줄을 차지하지 않는 요소다. 화면에 표시되는 만큼만 영역을 차지하고 나머지 공간에는 다른 요소가 올 수 있다. 따라서 한 줄에 여러 인라인 레벨 요소가 올 수 있다.

 종류 | 해당 태그 
--- | ---
블록 레벨 태그 | `<p>, <h1>~<h6>, <ul>, <ol>, <div>, <blockquote>, <form>, <hr>, <table>, <fieldset>, <address>`
인라인 레벨 태그 | `<img>, <object>, <br>, <sub>, <sup>, <span>, <input>, <textarea>, <label>, <button>`

### `width, height` 속성: 콘텐츠 영역의 크기

`width`는 박스의 너비, `height`은 박스의 높이를 결정한다. 속성 값을 적는 방법은 두 가지다. 픽셀(px) 단위로 적거나 백분율(%) 단위로 적는 것이다.

속성 값 | 설명
--- | ---
<px, cm...> | 고정 너비와 높이. 정해진 값 만큼의 크기를 만든다.
<%> | 가변 너비와 높이. 웹문서 창의 크기에 대한 비율로 크기를 만든다.

### `display` 속성: 화면 배치 방법 결정하기

`display`속성을 사용하면 블록 레벨 요소와 인라인 레벨 요소를 서로 바꿀 수 있다. 이런 방법은 언제 필요할까? 세로로 표시되는 리스트를 가로 내비게이션으로 바꿀 때, 한 줄로 표시되는 이미지들을 갤러리처럼 배치할 때 사용한다.

`display: block`: 해당 요소를 블록 레벨로 지정한다.



`display: inline`: 해당 요소를 인라인 레벨로 지정한다. 리스트에 `inline`을 지정하면 항목을 한 줄로 배치할 수 있다.

```html
<style>
nav ul li {
	display: inline;
    }
</style>
...
<nav>
      <ul>
      	<li><a href="#">국어</a></li>
      	<li><a href="#">수학</a></li>
      	<li><a href="#">영어</a></li>
      </ul>
</nav>

```

### `display: inline-block`

요소를 인라인 레벨로 배치하면서 내용에는 블록 레벨 속성을 지정할 때 사용한다. 

```html
<style>
nav ul li {
	display: inline-block;
	margin: 20px;
    }
</style>

```

### `display: none`, `visibility: hidden`

`display: none`은 해당 요소를 화면에서 아예 표시하지 않는다. 반면 `visibility: hidden`은 화면에서 요소를 감추기만 할 뿐 공간은 그대로 차지한다. 




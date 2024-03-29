package com.pandaboxdesign.todo;

import java.util.ArrayList;


import android.app.Activity;
import android.os.Bundle;
import android.util.SparseBooleanArray;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.view.inputmethod.EditorInfo;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;

public class MainActivity extends Activity{

	ArrayList<String> taskList = new ArrayList<String>();
	ArrayAdapter<String> taskAdapter;


	@Override
	public void onCreate(Bundle savedInstanceState) {
		this.requestWindowFeature(Window.FEATURE_NO_TITLE);
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		taskAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_multiple_choice, taskList);
		ListView myList = (ListView)findViewById(R.id.toDos);
		myList.setAdapter(taskAdapter);
		EditText editText = (EditText) findViewById(R.id.add_here);
		editText.setOnClickListener(sendListener);
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.activity_main, menu);
		return true;
	}
	
	/**
	 * Called when user finishes adding a task and clicks send.
	 */
	private OnClickListener sendListener = new OnClickListener(){
		public void onClick(View v){
			EditText editText = (EditText) findViewById(R.id.add_here);
			editText.setOnEditorActionListener(new OnEditorActionListener() {
			    public boolean onEditorAction(TextView v, int actionId,
						KeyEvent event) {
			    	EditText editText = (EditText) findViewById(R.id.add_here);
					if (actionId == EditorInfo.IME_ACTION_SEND){
				    	String newTask = editText.getText().toString();
				    	if (!(newTask.isEmpty())){
					    	taskList.add(newTask);
					    	taskAdapter.notifyDataSetChanged();
					    	editText.setText(null);
					    	return true;
				    	}
					}
					return false;
				}
			});
		}
	};
	
	/**
	 * Called when user clicks Finish
	 */
	public void clearDone(View view){
		ListView myList = (ListView)findViewById(R.id.toDos);
		SparseBooleanArray checkedItemPositions = myList.getCheckedItemPositions();
		int itemCount = myList.getCount();
		for (int i=itemCount-1; i>=0; i--){
			if (checkedItemPositions.get(i)){
				myList.setItemChecked(i, false);
				taskAdapter.remove(taskList.get(i));
			}
		}
		taskAdapter.notifyDataSetChanged();
	}
}

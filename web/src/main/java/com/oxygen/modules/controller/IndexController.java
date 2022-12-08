package com.oxygen.modules.controller;


import com.oxygen.modules.annotation.PermissionLimit;
import com.oxygen.modules.common.vo.R;
import com.oxygen.modules.service.IndexService;
import com.oxygen.modules.service.LoginService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.propertyeditors.CustomDateEditor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;

@Controller
public class IndexController {
    Logger logger = LoggerFactory.getLogger(getClass());
    @Resource
    IndexService indexService;
    @Resource
    private LoginService loginService;

    @RequestMapping("/")
    public String index(Model model) {
        Map<String, Object> dashboardMap = indexService.dashboardInfo();
        model.addAllAttributes(dashboardMap);
        return "index";
    }

    @RequestMapping("/toLogin")
    @PermissionLimit(limit=false)
    public String toLogin(HttpServletRequest request, HttpServletResponse response) {
        if (loginService.ifLogin(request, response) != null) {
            return "redirect:/";
        }
        return "login";
    }

    @RequestMapping(value="login", method= RequestMethod.POST)
    @ResponseBody
    @PermissionLimit(limit=false)
    public R loginDo(HttpServletRequest request, HttpServletResponse response, String userName, String password, String ifRemember){
        boolean ifRem = (ifRemember!=null && ifRemember.trim().length()>0 && "on".equals(ifRemember))?true:false;
        return loginService.login(request, response, userName, password, ifRem);
    }

    @RequestMapping(value="logout", method=RequestMethod.POST)
    @ResponseBody
    @PermissionLimit(limit=false)
    public R logout(HttpServletRequest request, HttpServletResponse response){
        return loginService.logout(request, response);
    }

    @RequestMapping("/page1")
    public String page1() throws IOException {
        return "subpage/page1";
    }
    @RequestMapping("/page2")
    public String page2() {
        return "subpage/page2";
    }
    @RequestMapping("/page3")
    public String page3() {
        return "subpage/page3";
    }

    @RequestMapping("/help")
    public String help() {
        return "help";
    }

    @InitBinder
    public void initBinder(WebDataBinder binder) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        dateFormat.setLenient(false);
        binder.registerCustomEditor(Date.class, new CustomDateEditor(dateFormat, true));
    }
}

package main

import (
	"github.com/gin-gonic/gin"
)

func GetProduct(ctx *gin.Context) {
	ctx.Writer.Write([]byte("true"))

}
func main() {
	r:=gin.Default()
	r.GET("/getOne",GetProduct)
	r.Run()
}
//压测工具 wrk
